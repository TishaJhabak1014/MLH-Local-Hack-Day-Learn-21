## About AI

### Topic: Transformer Neural Nets

RNN or Recurrent Neural Networks are feed-forward neural networks rolled out over time as such they deal with input data where the input has some defined ordering. This gives rise to several types of architecture as follows:
### Vector-Sequence Models: These takes fixed size vector as input and outputs a sequence of any length. For instance, in image captioning, the input can be a vector representation of an image and the output sequence is a senance that describes the image.
### Sequece-Vector Models: These neural networks take in sequences input and spits out a fixed line vector. For example, in sentiment analysis, the movie review is an input and a fixed size of vector is the output indicatind how good or bad this person thought the movie was.
### sequence-Sequence Models: Popular variant of RNNs take in a sequence of input and outputs another sequence. For example, language translation, the input can be a sentance in spanish and the output is the translation in english.

Thus, having a time-series data for the model, RNNs would be the goto. However, RNNs have some problem, like RNNs are slow so we use a truncated version of back propagation to train it, even which is hardware-intense. They can not deal with long sequences very well, we get gradients that vanish and explode if the network is too long.

## LSTM 
This introduced a long-short term mermory cell in place of dumb neurons. This cell has a branch that allows passed information to skip a lot of the processing of the current cell and move on to the next. This allows the memory to be retained for longer sequences. We seem to be able to deal with longer sequences or are we? However, in the first place, normal RNNs are slow but LSTMs are even slower. they are more cpmplex. For these RNNs and LSTMs, input data needs to be passed sequentially or serially one after the other. We need input of the previous state to make any operations on the current state. Such sequential flow just not make use of today's GPUs very well, which are designed for parallel computation. How can we use parallelization for sequential data?

## Transformers
Introduced in 2017, the transformer NN employs an encoder decoder architect like RNNs. The difference is that the input sequence in this can be passed in parallel unlike RNNs.
