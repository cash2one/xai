

#calss header
class _INTEGRAL():
	def __init__(self,): 
		self.name = "INTEGRAL"
		self.jsondata = {}

		self.parents = []
		self.childen = []

	def run(self, obj1, obj2):
		jsondata[obj2] = {}
		jsondata[obj2]['properties'] = self.name.lower()
		return jsondata