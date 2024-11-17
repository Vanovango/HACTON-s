import pandas as pd
from tensorflow.keras.layers import Dense, Embedding, GlobalMaxPooling1D, Conv1D
from tensorflow.keras.models import Sequential
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.preprocessing.text import Tokenizer

from Save import save_person
from Chose_team import task_form

save = save_person.Save_Resume()



########################################################################################################################
# # Вставка в таблицу
def input_resume_in_bd(cursor, db, name, date_of_birth, phone_number, resume):
    temp = skils_score(resume)

    cursor.execute(
        f"INSERT INTO _resume VALUES ('{name}', '{date_of_birth}', '{phone_number}', '{temp[0]}',"
        f" '{temp[1]}', '{temp[2]}', '{temp[3]}', '{temp[4]}', '{temp[5]}', '{temp[6]}', '{temp[7]}', '{temp[8]}',"
        f" '{temp[9]}', '{temp[10]}', '{temp[11]}', '{resume}')")
    db.commit()


########################################################################################################################
# #Вывод содержимого таблицы
def show_data_in_bd(cursor):
    cursor.execute(f"SELECT * FROM _resume")
    return cursor.fetchall()


########################################################################################################################
def delete_person(cursor, db):
    name = str(input('Enter name for delete:'))
    cursor.execute(f"DELETE from _resume WHERE name = '{name}' ")
    db.commit()


########################################################################################################################
# Применяем класификацию с помощью нейронки
def skils_score(resume):
    model_cnn_weights = "C:\\Users\\voyte\Desktop\\Python Progects\Hacaton\\ready_models\\best_resum_model.h5"
    # Максимальное количество слов
    num_words = 10000
    # Максимальная длина комментария
    max_resum_len = 100

    # Создаем токенизатор
    train = pd.read_excel("C:\\Users\\voyte\\Desktop\\Python Progects\\Hacaton\\train_models_code\\data_resume.xlsx")
    data_resumes = train['resume']
    tokenizer = Tokenizer(num_words=num_words)
    tokenizer.fit_on_texts(data_resumes)
    # Преобразуем резюме в числовое представление
    sequence = tokenizer.texts_to_sequences(resume)

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

    # Загружаем веса и применяем сверточную сеть
    data = pad_sequences(sequence, maxlen=max_resum_len)
    model_cnn.load_weights(model_cnn_weights)
    result = model_cnn.predict(data)
    skils = [int(i * 100000) for i in result[0]]
    return skils


########################################################################################################################

def find_skil_for_task(task):

    model_cnn_weights = "C:\\Users\\voyte\Desktop\\Python Progects\Hacaton\\ready_models\\best_task_model.h5"
    # Максимальное количество слов
    num_words = 10000
    # Максимальная длина комментария
    max_task_len = 30
    # Количество классов
    nb_classes = 12

    # Создаем токенизатор
    train = pd.read_excel("C:\\Users\\voyte\\Desktop\\Python Progects\\Hacaton\\train_models_code\\data_task.xlsx")
    data_tasks = train['task']
    tokenizer = Tokenizer(num_words=num_words)
    tokenizer.fit_on_texts(data_tasks)
    # Преобразуем задачу в числовое представление
    sequence = tokenizer.texts_to_sequences(task)

    # Сверточная сеть
    model_cnn = Sequential()
    model_cnn.add(Embedding(num_words, 32, input_length=max_task_len))
    model_cnn.add(Conv1D(250, 5, padding='valid', activation='relu'))
    model_cnn.add(GlobalMaxPooling1D())
    model_cnn.add(Dense(128, activation='relu'))
    model_cnn.add(Dense(12, activation='softmax'))

    model_cnn.compile(optimizer='adam',
                      loss='categorical_crossentropy',
                      metrics=['accuracy'])

    # Загружаем веса и применяем сверточную сеть
    data = pad_sequences(sequence, maxlen=max_task_len)
    model_cnn.load_weights(model_cnn_weights)
    result = model_cnn.predict(data)

    print(result)

    if result.index(result.max()) == 0:
        print(result.index(result.max()))
        return 'programming'
    elif result.index(result.max()) == 1:
        print(result.index(result.max()))
        return 'physics'
    elif result.index(result.max()) == 2:
        print(result.index(result.max()))
        return 'mathematics'
    elif result.index(result.max()) == 3:
        print(result.index(result.max()))
        return 'engineer'
    elif result.index(result.max()) == 4:
        print(result.index(result.max()))
        return 'lawyer'
    elif result.index(result.max()) == 5:
        print(result.index(result.max()))
        return 'analytics'
    elif result.index(result.max()) == 6:
        print(result.index(result.max()))
        return 'work_organization'
    elif result.index(result.max()) == 7:
        print(result.index(result.max()))
        return 'sociability'
    elif result.index(result.max()) == 8:
        print(result.index(result.max()))
        return 'independence'
    elif result.index(result.max()) == 9:
        print(result.index(result.max()))
        return 'stress_resistance'
    elif result.index(result.max()) == 10:
        print(result.index(result.max()))
        return 'initiative'
    elif result.index(result.max()) == 11:
        print(result.index(result.max()))
        return 'physical_abilities'

#######################################################################################################################
#     1 name text,
#     2 date_of_birth text,
#     3 phone_number integer,
#     4 programming integer,
#     5 physics integer,
#     6 mathematics integer,
#     7 engineer integer,
#     8 lawyer integer,
#     9 analytics integer,
#     10 work_organization integer,
#     11 sociability integer,
#     12 independence integer,
#     13 stress_resistance integer,
#     14 initiative integer,
#     15 physical_abilities integer
#     16 resume text,
