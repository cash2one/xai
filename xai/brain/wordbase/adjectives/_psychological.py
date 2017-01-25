

#calss header
class _PSYCHOLOGICAL():
	def __init__(self,): 
		self.name = "PSYCHOLOGICAL"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
