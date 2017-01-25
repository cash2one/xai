

#calss header
class _INFANT():
	def __init__(self,): 
		self.name = "INFANT"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
