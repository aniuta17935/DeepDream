import tensorflow as tf
import numpy as np
import PIL.Image

def download(file_path, max_dim=None):
    img = PIL.Image.open(file_path)
    if max_dim:
        img.thumbnail((max_dim, max_dim))
    return np.array(img)


def tensor_to_image(tensor):
    tensor = tensor*255
    tensor = np.array(tensor, dtype=np.uint8)
    if np.ndim(tensor) > 3:
        assert tensor.shape[0] == 1
        tensor = tensor[0]
    return PIL.Image.fromarray(tensor)


def calc_loss(img, model):
  img_batch = tf.expand_dims(img, axis=0)
  layer_activations = model(img_batch)
  if len(layer_activations) == 1:
    layer_activations = [layer_activations]

  losses = []
  for act in layer_activations:
    loss = tf.math.reduce_mean(act)
    losses.append(loss)

  return tf.reduce_sum(losses)

class DeepDream(tf.Module):
  def __init__(self, model):
    self.model = model

  @tf.function(
      input_signature=(
        tf.TensorSpec(shape=[None,None,3], dtype=tf.float32),
        tf.TensorSpec(shape=[], dtype=tf.int32),
        tf.TensorSpec(shape=[], dtype=tf.float32),)
  )
  def __call__(self, img, steps, step_size):
      print("Tracing")
      loss = tf.constant(0.0)
      for n in tf.range(steps):
        with tf.GradientTape() as tape:
          tape.watch(img)
          loss = calc_loss(img, self.model)

        gradients = tape.gradient(loss, img)

        gradients /= tf.math.reduce_std(gradients) + 1e-8 

        img = img + gradients*step_size
        img = tf.clip_by_value(img, -1, 1)

      return loss, img

def run_deep_dream(path, level = 1, steps=100, step_size=0.01):
  base_model = tf.keras.applications.InceptionV3(include_top=False, weights='imagenet')
  names = [f'mixed{level}', f'mixed{str(int(level)+1)}']
  print(names)
  layers = [base_model.get_layer(name).output for name in names]
  dream_model = tf.keras.Model(inputs=base_model.input, outputs=layers)
  deepdream = DeepDream(dream_model)

  img = download(path, max_dim=500)
  img = tf.keras.applications.inception_v3.preprocess_input(img)
  img = tf.convert_to_tensor(img)
  step_size = tf.convert_to_tensor(step_size)
  steps_remaining = steps
  step = 0
  while steps_remaining:
    if steps_remaining > 100:
      run_steps = tf.constant(100)
    else:
      run_steps = tf.constant(steps_remaining)
    steps_remaining -= run_steps
    step += run_steps

    loss, img = deepdream(img, run_steps, tf.constant(step_size))
    print("Step {}, loss {}".format(step, loss))
  return tensor_to_image(img)
