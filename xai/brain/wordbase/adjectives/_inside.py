

#calss header
class _INSIDE():
	def __init__(self,): 
		self.name = "INSIDE"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
