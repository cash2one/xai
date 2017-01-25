

#calss header
class _SIDE():
	def __init__(self,): 
		self.name = "SIDE"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
