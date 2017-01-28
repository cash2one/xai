

#calss header
class _REAL():
	def __init__(self,): 
		self.name = "REAL"
		self.definitions = [u'existing in fact and not imaginary: ', u'the value of earnings, etc. after the effect of rising prices is considered: ', u'after considering things that affect what a number or amount really means, such as the effect of rising prices: ', u'things as they really are, not as they exist in the imagination, in a story, on the internet, etc.: ', u'being what it appears to be and not false: ', u'(especially of foods) produced using traditional methods and without artificial substances: ', u'real, not pretended: ', u'the most important; the main: ', u'used to emphasize a noun: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
