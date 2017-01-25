

#calss header
class _ADDITIONAL():
	def __init__(self,): 
		self.name = "ADDITIONAL"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
