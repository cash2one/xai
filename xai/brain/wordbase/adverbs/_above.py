

#calss header
class _ABOVE():
	def __init__(self,): 
		self.name = "ABOVE"
		self.definitions = [u'in or to a higher position than something else: ', u'more than an amount or level: ', u'most importantly: ', u'in a more important or advanced position than someone else: ', u'too good or important for something: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
