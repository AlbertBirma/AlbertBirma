import numpy as np 

users_stats = np.array([], np.int32)
next_user_stats = np.array([0, 1, 2, 0, 0, 0])
  
def similarity(users_matrix, new_user_data, similarities = []):
    for array in users_matrix:
        array_length = np.linalg.norm(array)
        user_array_length = np.linalg.norm(new_user_data)
        array_dot = np.dot(new_user_data, array)
        similarity_percent = (array_dot) / ( array_length * user_array_length )
        similarities.append(similarity_percent)
    for element in list(enumerate(similarities)):
        if max(similarities) in element:
            print(f'User with id №{element[0]} is the most similar to a new user.')
        
similarity(users_stats, next_user_stats)
