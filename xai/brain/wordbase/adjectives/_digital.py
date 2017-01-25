

#calss header
class _DIGITAL():
	def __init__(self,): 
		self.name = "DIGITAL"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
