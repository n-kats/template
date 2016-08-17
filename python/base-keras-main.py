import keras.models import Seqential
import keras.layers import Dense, Merge
model = Seqential([])
model.compile(optimizer='rmsprop',
		loss='categorical_crossentropy',
		metrics=['accuracy'])
model.fit() # TODO
