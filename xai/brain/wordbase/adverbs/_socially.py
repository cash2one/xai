

#calss header
class _SOCIALLY():
	def __init__(self,): 
		self.name = "SOCIALLY"
		self.definitions = [u'in or relating to a social situation: ', u'by or relating to society: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
