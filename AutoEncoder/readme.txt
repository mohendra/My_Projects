
This is an autoencoder program. 
The detail of the architechture is as follows. 

Architechture of the AutoEncoder:
Here we will design a convolutional neural network for the AutoEncoder. The structure of the neural network will be as follows:
The Architecture of the AutoEncoder:

· · · · · · · · · ·     -- I (input data, 1-deep) X [batch, 28, 28, 1]

@ @ @ @ @ @ @ @ @ @ @   -- 1st Encoder conv. layer of: 10x10x1=>10 stride 1,SAME Padding WE1[10, 10, 1, 10],B1[10]
                           Note: All Convolution Layers will be activated with Relu
\/\/\/\/\/\/\/\/\/\/    -- Max pool with kernal[1,2,2,1] and stride [1,2,2,1], SAME Padding                        
∶∶∶∶∶∶∶∶∶∶∶∶∶∶∶∶∶∶    -- E1 [batch, 14, 14, 10](This is the output of the 1st Encoder convolution layer)

  @ @ @ @ @ @ @ @       -- 2nd Encoder conv. layer of: 5x5x10=>10 stride 1,SAME Padding WE2 [5, 5, 10, 10],B2[10]
  \/\/\/\/\/\/\/        -- Max pool with kernal[1,2,2,1] and stride [1,2,2,1], SAME Padding
  ∶∶∶∶∶∶∶∶∶∶∶∶∶∶       -- E2 [batch, 7, 7, 10]


   XXXXXXXXXXX        -- End of Encoder and Start of Decoder, Now for decoding we have to upsample the output
                         using: {upsample1 = tf.image.resize_images(E3, size=(14,14), 
                                                                 method=tf.image.ResizeMethod.NEAREST_NEIGHBOR)}
   ^^^^^^^^^^^        -- U1 Upsampling [Batch, 14, 14, 10]                                                              
   @ @ @ @ @ @        -- 1st Decoder conv. layer of: 5x5x10=>10 stride 1,SAME Padding WD1[5, 5, 10, 10],C1[10] 
 
 ∶∶∶∶∶∶∶∶∶∶∶∶∶∶∶     -- D1 [batch, 14, 14, 10] (This is the output of the 1st Decoder convolution layer)
  ^^^^^^^^^^^^^^^     -- U2 Upsampling of D1 to size [Batch, 28,28, 10] 

@ @ @ @ @ @ @ @ @     -- 2nd Decoder conv.layer of: 10x10x10=>10 stride1,SAME Padding WD2[10, 10, 10, 10],C2[10]
∶∶∶∶∶∶∶∶∶∶∶∶∶∶∶:::    -- D2 [batch, 10, 10, 10]

...................   -- Logits ConV. Layer of: 10X10X10=>1 stride 1,SAME Padding, WD3 [10, 10,10,1], C3 [1] 

                         Pass the logits through Sigmoid tf.nn.sigmoid(logits)for reconstruction.
