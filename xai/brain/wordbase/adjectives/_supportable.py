

#calss header
class _SUPPORTABLE():
	def __init__(self,): 
		self.name = "SUPPORTABLE"
		self.definitions = [u'A supportable argument, statement, etc. can be shown to be true using evidence.', u'If something bad is supportable, you are able to accept it or continue despite it: ', u'used to describe an activity that can continue without problems: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
