

#calss header
class _ACADEMIC():
	def __init__(self,): 
		self.name = "ACADEMIC"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
