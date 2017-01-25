

#calss header
class _DEPENDENT():
	def __init__(self,): 
		self.name = "DEPENDENT"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
