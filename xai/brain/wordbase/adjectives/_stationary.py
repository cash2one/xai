

#calss header
class _STATIONARY():
	def __init__(self,): 
		self.name = "STATIONARY"
		self.jsondata = {}

		self.parents = []
		self.childen = []

	def run(self, obj1, obj2):
		jsondata[obj2] = {}
		jsondata[obj2]['properties'] = self.name.lower()
		return jsondata
