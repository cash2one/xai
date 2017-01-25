

#calss header
class _SHUT():
	def __init__(self,): 
		self.name = "SHUT"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
