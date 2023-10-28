import zlib,json,cv2
import numpy as np

def compress_and_encode_data(keypoints, descriptors):
    keypoints = keypoints[::9]
    descriptors = descriptors[::9]
    # Chuyển đổi keypoints từ các đối tượng KeyPoint thành mảng numpy
    keypoints_list = [(kp.pt[0], kp.pt[1], kp.size, kp.angle, kp.response, kp.octave, kp.class_id) for kp in keypoints]
    descriptors = descriptors.tolist()
    # print(descriptors)
    data = {
        'keypoints': keypoints_list,
        'descriptors': descriptors,
    }
    serialized_data = json.dumps(data).encode('utf-8')

    compressed_data = zlib.compress(serialized_data, 9)
    return compressed_data

def decompress_zlib_data(encoded_data):
    decompressed_data = zlib.decompress(encoded_data)  
    data = decompressed_data.decode('utf-8')  
    decoded_data = json.loads(data)  
    return decoded_data

def convert_to_keypoints(data):
    keypoints_data = data['keypoints']
    keypoints = [cv2.KeyPoint(*kp_data) for kp_data in keypoints_data]
    stored_keypoints = tuple(keypoints)
    return stored_keypoints

def convert_to_descriptors(data):
    descriptors_data = data['descriptors']
    descriptors = np.array(descriptors_data)
    stored_descriptors = descriptors.astype(np.float32)
    return stored_descriptors