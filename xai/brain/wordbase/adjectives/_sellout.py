

#calss header
class _SELLOUT():
	def __init__(self,): 
		self.name = "SELLOUT"
		self.jsondata = {}

		self.parents = []
		self.childen = []

	def run(self, obj1, obj2):
		jsondata[obj2] = {}
		jsondata[obj2]['properties'] = self.name.lower()
		return jsondata
