

#calss header
class _MIRRORED():
	def __init__(self,): 
		self.name = "MIRRORED"
		self.jsondata = {}

		self.parents = []
		self.childen = []

	def run(self, obj1, obj2):
		jsondata[obj2] = {}
		jsondata[obj2]['properties'] = self.name.lower()
		return jsondata