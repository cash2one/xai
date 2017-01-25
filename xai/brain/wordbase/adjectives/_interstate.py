

#calss header
class _INTERSTATE():
	def __init__(self,): 
		self.name = "INTERSTATE"
		self.jsondata = {}

		self.parents = []
		self.childen = []

	def run(self, obj1, obj2):
		jsondata[obj2] = {}
		jsondata[obj2]['properties'] = self.name.lower()
		return jsondata
