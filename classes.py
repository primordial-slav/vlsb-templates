import imgaug
import tensorflow as tf

class TFAugment:
    'Used for annoying use of tf.numpy_function when in combination with imgaug'
    def __init__(self,seq,**kwargs):
        self.seq = seq

    def aug_fn(self,):
        images, points= self.seq(image=images, keypoints=points)
        return images, points
    
    def augment(self,images):
        img_dtype = images.dtype
        img_shape = tf.shape(images)
        
        pts_dtype = pts.dtype
        pts_shape = tf.shape(pts)
        pts = tf.expand_dims(pts, axis=0)
        images, pts = tf.numpy_function(self.aug_fn,
                                [images,pts],
                                [img_dtype,pts_dtype])
        
        images = tf.reshape(images, shape = img_shape)
        #pts = tf.reshape(pts, shape = pts_shape)
        pts = tf.reshape(pts, shape = (2,2))
        return images, pts