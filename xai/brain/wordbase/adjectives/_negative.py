

#calss header
class _NEGATIVE():
	def __init__(self,): 
		self.name = "NEGATIVE"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
