

from xai.brain.wordbase.nouns._glossary import _GLOSSARY

#calss header
class _GLOSSARIES(_GLOSSARY, ):
	def __init__(self,): 
		_GLOSSARY.__init__(self)
		self.name = "GLOSSARIES"
		self.specie = 'nouns'
		self.basic = "glossary"
		self.jsondata = {}
