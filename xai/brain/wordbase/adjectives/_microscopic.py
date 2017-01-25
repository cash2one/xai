

#calss header
class _MICROSCOPIC():
	def __init__(self,): 
		self.name = "MICROSCOPIC"
		self.jsondata = {}

		self.parents = []
		self.childen = []

	def run(self, obj1, obj2):
		jsondata[obj2] = {}
		jsondata[obj2]['properties'] = self.name.lower()
		return jsondata
