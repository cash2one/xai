

#calss header
class _FRENCH():
	def __init__(self,): 
		self.name = "FRENCH"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
