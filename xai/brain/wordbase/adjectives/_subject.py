

#calss header
class _SUBJECT():
	def __init__(self,): 
		self.name = "SUBJECT"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
