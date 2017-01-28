

#calss header
class _IRREGULAR():
	def __init__(self,): 
		self.name = "IRREGULAR"
		self.definitions = [u'(of behaviour or actions) not according to usual rules or what is expected: ', u'An irregular verb, noun, adjective, etc. does not obey the usual rules for words in the language.', u'not regular in shape or form; having parts of different shapes or sizes: ', u'not happening at regular times or not with regular spaces in between: ', u'not emptying your bowels as often as you would usually', u'(of a soldier) fighting for a country but not as a member of its official army']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
