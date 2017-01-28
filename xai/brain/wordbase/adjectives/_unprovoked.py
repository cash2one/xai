

#calss header
class _UNPROVOKED():
	def __init__(self,): 
		self.name = "UNPROVOKED"
		self.definitions = [u'If an unpleasant action or remark is unprovoked, it has not been caused by anything and is therefore unfair: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
