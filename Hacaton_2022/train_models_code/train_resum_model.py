import pandas as pd
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Embedding, MaxPooling1D, Dropout, LSTM, Bidirectional, SpatialDropout1D, GlobalMaxPooling1D, Conv1D
from tensorflow.keras.callbacks import ModelCheckpoint
from tensorflow.keras import utils
import matplotlib.pyplot as plt



# Максимальное количество слов
num_words = 10000
# Максимальная длина комментария
max_resum_len = 100

train = pd.read_excel("data_resume.xlsx")
resumes = train['resume']

y_train = train[['programming', 'physics', 'mathematics', 'engineer', 'lawyer', 'analytics',
                 'work_organization', 'sociability', 'independence', 'stress_resistance', 'initiative',
                 'physical_abilities']]

# Создаем токенизатор
tokenizer = Tokenizer(num_words=num_words)
tokenizer.fit_on_texts(resumes)
#Преобразуем резюме в числовое представление
sequences = tokenizer.texts_to_sequences(resumes)

#Ограничиваем длину резюме
x_train = pad_sequences(sequences, maxlen=max_resum_len)

# Сверточная сеть
model_cnn = Sequential()
model_cnn.add(Embedding(num_words, 64, input_length=max_resum_len))
model_cnn.add(Conv1D(250, 5, padding='valid', activation='relu'))
model_cnn.add(GlobalMaxPooling1D())
model_cnn.add(Dense(128, activation='relu'))
model_cnn.add(Dense(12, activation='sigmoid'))

model_cnn.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])

#Создаем callback для сохранения нейронной сети на каждой эпохе,
# если качество работы на проверочном наборе данных улучшилось. Сеть сохраняется в файл best_resum_model.h5
model_cnn_save_path = '../ready_models/best_resum_model.h5'
checkpoint_callback_lstm = ModelCheckpoint(model_cnn_save_path,
                                      monitor='val_accuracy',
                                      save_best_only=True,
                                      verbose=1)

history_lstm = model_cnn.fit(x_train,
                              y_train,
                              epochs=1,
                              batch_size=512,
                              validation_split=0.2,
                              callbacks=[checkpoint_callback_lstm])

model_cnn.load_weights(model_cnn_save_path)

#Покажем результат обучения на графике
# plt.plot(history_lstm.history['accuracy'],
#          label='Доля верных ответов на обучающем наборе')
# plt.plot(history_lstm.history['val_accuracy'],
#          label='Доля верных ответов на проверочном наборе')
# plt.xlabel('Эпоха обучения')
# plt.ylabel('Доля верных ответов')
# plt.legend()
# plt.show()

def test(line):
    sequence = tokenizer.texts_to_sequences([line])
    data = pad_sequences(sequence, maxlen=max_resum_len)
    model_cnn.load_weights(model_cnn_save_path)
    result = model_cnn.predict(data)
    print(*result)
    print('----------------------')
    print(result[0])

test('Я работал программистом около 5 лет, знаю несколько языков программирования, Rython, C++. '
           'Так же я хорошо общаюсь с людьми, могу найти общий язык с любым человеком.'
           'Забыл сказать, в детстве я занимался спортом, это привело к моей хорошей физической форме')