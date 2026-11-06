import numpy as np

def cosine_similarity(v1, v2):
	dot_product = np.dot(v1,v2)

	magnitude_v1 = np.linalg.norm(v1)
	magnitude_v2 = np.linalg.norm(v2)

	if magnitude_v1 == 0 or magnitude_v2 == 0:
		return 0.0
	
	similarity = dot_product/(magnitude_v1*magnitude_v2)

	return float(similarity)