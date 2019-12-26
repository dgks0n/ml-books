# force a channel ordering
from keras import backend
# force channels-first ordering
backend.set_image_dim_ordering('th')
print(backend.image_data_format())
# force channels-last ordering
backend.set_image_dim_ordering('tf')
print(backend.image_data_format())