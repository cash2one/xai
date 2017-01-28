

#calss header
class _IMMEDIATE():
	def __init__(self,): 
		self.name = "IMMEDIATE"
		self.definitions = [u'happening or done without delay or very soon after something else: ', u'used to refer to something or someone that is close to, or is a cause of or an effect of, something or someone else: ', u'in the present or as soon as possible: ', u'the period of time that is coming next', u'your closest relations, such as your parents, children, husband, or wife']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
