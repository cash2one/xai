

#calss header
class _INTRAVENOUSLY():
	def __init__(self,): 
		self.name = "INTRAVENOUSLY"
		self.jsondata = {}

		self.parents = []
		self.childen = []

	def run(self, obj1, obj2):
		jsondata[obj2] = {}
		jsondata[obj2]['properties'] = self.name.lower()
		return jsondata
