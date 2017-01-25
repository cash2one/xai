

#calss header
class _RID():
	def __init__(self,): 
		self.name = "RID"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
