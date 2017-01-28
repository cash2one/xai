

#calss header
class _TACKY():
	def __init__(self,): 
		self.name = "TACKY"
		self.definitions = [u'of cheap quality or in bad style: ', u'sticky; (especially of paint or glue) not completely dry']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
