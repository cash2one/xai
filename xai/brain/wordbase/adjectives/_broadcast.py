

#calss header
class _BROADCAST():
	def __init__(self,): 
		self.name = "BROADCAST"
		self.jsondata = {}

		self.parents = []
		self.childen = []

	def run(self, obj1, obj2):
		jsondata[obj2] = {}
		jsondata[obj2]['properties'] = self.name.lower()
		return jsondata
