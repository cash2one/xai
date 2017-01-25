

#calss header
class _OVERDUE():
	def __init__(self,): 
		self.name = "OVERDUE"
		self.jsondata = {}

		self.parents = []
		self.childen = []

	def run(self, obj1, obj2):
		jsondata[obj2] = {}
		jsondata[obj2]['properties'] = self.name.lower()
		return jsondata
