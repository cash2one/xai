

#calss header
class _DESIRABLE():
	def __init__(self,): 
		self.name = "DESIRABLE"
		self.definitions = [u'worth having and wanted by most people: ', u'sexually attractive: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
