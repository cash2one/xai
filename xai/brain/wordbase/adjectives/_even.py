

#calss header
class _EVEN():
	def __init__(self,): 
		self.name = "EVEN"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
