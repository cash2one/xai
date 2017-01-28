

#calss header
class _ILL():
	def __init__(self,): 
		self.name = "ILL"
		self.definitions = [u'badly: ', u'to say unkind things about someone: ', u'to be a sign of bad things in the future: ', u'If you can ill afford to do something, it will cause problems for you if you do it: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
