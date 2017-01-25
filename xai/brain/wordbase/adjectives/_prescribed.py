

#calss header
class _PRESCRIBED():
	def __init__(self,): 
		self.name = "PRESCRIBED"
		self.jsondata = {}

		self.parents = []
		self.childen = []

	def run(self, obj1, obj2):
		jsondata[obj2] = {}
		jsondata[obj2]['properties'] = self.name.lower()
		return jsondata
