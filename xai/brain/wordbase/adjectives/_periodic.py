

#calss header
class _PERIODIC():
	def __init__(self,): 
		self.name = "PERIODIC"
		self.jsondata = {}

		self.parents = []
		self.childen = []

	def run(self, obj1, obj2):
		jsondata[obj2] = {}
		jsondata[obj2]['properties'] = self.name.lower()
		return jsondata
