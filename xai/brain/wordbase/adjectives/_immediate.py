

#calss header
class _IMMEDIATE():
	def __init__(self,): 
		self.name = "IMMEDIATE"
		self.jsondata = {}

		self.parents = []
		self.childen = []

	def run(self, obj1, obj2):
		jsondata[obj2] = {}
		jsondata[obj2]['properties'] = self.name.lower()
		return jsondata
