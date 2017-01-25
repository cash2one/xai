

#calss header
class _ACOUSTIC():
	def __init__(self,): 
		self.name = "ACOUSTIC"
		self.jsondata = {}

		self.parents = []
		self.childen = []

	def run(self, obj1, obj2):
		jsondata[obj2] = {}
		jsondata[obj2]['properties'] = self.name.lower()
		return jsondata
