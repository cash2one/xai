

#calss header
class _PRECEDING():
	def __init__(self,): 
		self.name = "PRECEDING"
		self.jsondata = {}

		self.parents = []
		self.childen = []

	def run(self, obj1, obj2):
		jsondata[obj2] = {}
		jsondata[obj2]['properties'] = self.name.lower()
		return jsondata
