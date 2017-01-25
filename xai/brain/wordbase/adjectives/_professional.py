

#calss header
class _PROFESSIONAL():
	def __init__(self,): 
		self.name = "PROFESSIONAL"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
