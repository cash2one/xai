

#calss header
class _ACTIONABLE():
	def __init__(self,): 
		self.name = "ACTIONABLE"
		self.jsondata = {}

		self.parents = []
		self.childen = []

	def run(self, obj1, obj2):
		jsondata[obj2] = {}
		jsondata[obj2]['properties'] = self.name.lower()
		return jsondata
