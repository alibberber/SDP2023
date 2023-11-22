import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from tensorflow.keras.preprocessing import image
from tensorflow.keras.preprocessing.image import img_to_array, load_img
import numpy as np

# Basit bir CNN modeli oluştur
model = Sequential()
model.add(Conv2D(32, (3, 3), input_shape=(64, 64, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Conv2D(32, (3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Flatten())
model.add(Dense(units=128, activation='relu'))
model.add(Dense(units=1, activation='sigmoid'))

# Modeli derle
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Modeli eğitim için örnek veri setiyle eğit
# Bu örnekte, eğitim için kullanılan veri seti örnek bir veri setidir.
# Gerçek bir projede daha büyük ve çeşitli bir veri seti kullanılmalıdır.
# Modelinizi daha iyi performans için daha uzun süre eğitmeniz gerekebilir.
# Eğitim sürecini optimize etmek için hiperparametreleri ayarlamanız gerekebilir.
# Ayrıca, modelinizi değerlendirmek ve doğrulamak için ayrı bir veri seti kullanmalısınız.

# Eğitim veri seti oluştur
# Bu örnekte, 'ateşli' ve 'ateşsiz' klasörlerinde bulunan resimler kullanılmıştır.
# Gerçek bir projede daha fazla çeşitlilik ve daha fazla veri önerilir.
from tensorflow.keras.preprocessing.image import ImageDataGenerator

train_datagen = ImageDataGenerator(rescale=1./255, shear_range=0.2, zoom_range=0.2, horizontal_flip=True)
training_set = train_datagen.flow_from_directory('veri_seti_yolu', target_size=(64, 64), batch_size=32, class_mode='binary')

# Modeli eğit
model.fit(training_set, epochs=25)

# Modeli kaydet
model.save('yangin_kontrol_modeli.h5')

# Eğitilen modeli kullanarak yangın kontrolü yap
def yangin_kontrolu_yap(file_path):
    test_image = image.load_img(file_path, target_size=(64, 64))
    test_image = image.img_to_array(test_image)
    test_image = np.expand_dims(test_image, axis=0)
    result = model.predict(test_image)
    if result[0][0] == 1:
        return "Ateş Algılandı!"
    else:
        return "Ateş Algılanmadı."

# Test et
test_resmi_yolu = 'ates.png'  # Kendi test resminizi kullanın
sonuc = yangin_kontrolu_yap(test_resmi_yolu)
print(sonuc)
